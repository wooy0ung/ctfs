.class public Lcom/didictf/hellolibs/MainActivity;
.super Landroid/support/v7/app/AppCompatActivity;
.source "MainActivity.java"


# instance fields
.field private mFlagEntryView:Landroid/widget/TextView;

.field private mFlagResultView:Landroid/widget/TextView;


# direct methods
.method static constructor <clinit>()V
    .locals 1

    .prologue
    .line 44
    const-string v0, "hello-libs"

    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V

    .line 45
    return-void
.end method

.method public constructor <init>()V
    .locals 0

    .prologue
    .line 26
    invoke-direct {p0}, Landroid/support/v7/app/AppCompatActivity;-><init>()V

    return-void
.end method


# virtual methods
.method public onClickTest(Landroid/view/View;)V
    .locals 2
    .param p1, "v"    # Landroid/view/View;

    .prologue
    .line 48
    iget-object v0, p0, Lcom/didictf/hellolibs/MainActivity;->mFlagEntryView:Landroid/widget/TextView;

    invoke-virtual {v0}, Landroid/widget/TextView;->getText()Ljava/lang/CharSequence;

    move-result-object v0

    invoke-interface {v0}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0}, Lcom/didictf/hellolibs/MainActivity;->stringFromJNI()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    .line 49
    iget-object v0, p0, Lcom/didictf/hellolibs/MainActivity;->mFlagResultView:Landroid/widget/TextView;

    const-string v1, "Correct"

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 53
    :goto_0
    return-void

    .line 51
    :cond_0
    iget-object v0, p0, Lcom/didictf/hellolibs/MainActivity;->mFlagResultView:Landroid/widget/TextView;

    const-string v1, "Wrong"

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_0
.end method

.method protected onCreate(Landroid/os/Bundle;)V
    .locals 1
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .prologue
    .line 36
    invoke-super {p0, p1}, Landroid/support/v7/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 37
    const v0, 0x7f04001a

    invoke-virtual {p0, v0}, Lcom/didictf/hellolibs/MainActivity;->setContentView(I)V

    .line 38
    const v0, 0x7f0b0055

    invoke-virtual {p0, v0}, Lcom/didictf/hellolibs/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    iput-object v0, p0, Lcom/didictf/hellolibs/MainActivity;->mFlagEntryView:Landroid/widget/TextView;

    .line 39
    const v0, 0x7f0b0057

    invoke-virtual {p0, v0}, Lcom/didictf/hellolibs/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    iput-object v0, p0, Lcom/didictf/hellolibs/MainActivity;->mFlagResultView:Landroid/widget/TextView;

    .line 41
    return-void
.end method

.method public native stringFromJNI()Ljava/lang/String;
.end method
